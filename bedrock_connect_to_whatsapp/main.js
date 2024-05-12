import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";
import { Client } from 'whatsapp-web.js';
import qrcode from 'qrcode-terminal';

 // Create a Bedrock Runtime client in the AWS Region of your choice.
 const bedrock_client = new BedrockRuntimeClient({ region: "us-east-1" });
 
 // Set the model ID, e.g., Llama 2 Chat 13B.
 const modelId = "meta.llama3-70b-instruct-v1:0";

const client = new Client({
    webVersionCache: {
      type: "remote",
      remotePath:
        "https://raw.githubusercontent.com/wppconnect-team/wa-version/main/html/2.2412.54.html",
    },
  });

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.initialize();

client.on('message_create', async (message) => {
	if (message.id.fromMe === false) {

    const temp = "Let's do a role play. You have the character of Albert Einstein but your name is Tim. You never break character. You respond to the following WhatsApp message and send nothing else that just the response: ";

    let message_for_prompt = temp.concat(message.body);
    const prompt = <s>[INST] ${message_for_prompt} [/INST];

    const request = {
      prompt,
      // Optional inference parameters:
      max_gen_len: 512,
      temperature: 0.5,
      top_p: 0.9,
    };
    
    // Encode and send the request.
    const response = await bedrock_client.send(
      new InvokeModelCommand({
        contentType: "application/json",
        body: JSON.stringify(request),
        modelId,
      }),
    );

    // Decode the native response body.
    /** @type {{ generation: string }} */
    const nativeResponse = JSON.parse(new TextDecoder().decode(response.body));

    // Extract and print the generated text.
    const responseText = nativeResponse.generation;
    
		client.sendMessage(message.from, responseText);

	}
});

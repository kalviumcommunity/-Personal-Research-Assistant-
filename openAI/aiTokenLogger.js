import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function askAI(prompt) {
  try {
    const response = await client.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: prompt }],
    });

    // Log AI's response
    console.log("AI Response:", response.choices[0].message.content);

    // Log token usage
    console.log("---- Token Usage ----");
    console.log("Prompt tokens:", response.usage.prompt_tokens);
    console.log("Completion tokens:", response.usage.completion_tokens);
    console.log("Total tokens:", response.usage.total_tokens);
    console.log("---------------------");

  } catch (error) {
    console.error("Error:", error);
  }
}

// Example call
askAI("Explain the impact of renewable energy on climate change in simple terms.");

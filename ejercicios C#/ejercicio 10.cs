using System;

namespace EjerciciosLogica
{
    class Programa
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== EJERCICIO 10: CUENTA REGRESIVA ===");
            EjecutarCuentaRegresiva();

            Console.WriteLine("\nPresiona cualquier tecla para salir...");
            Console.ReadKey();
        }

        static void EjecutarCuentaRegresiva()
        {
            int contador = 10;


            while (contador >= 1)
            {
                Console.WriteLine(contador);
                
                contador--; 
            }

            Console.WriteLine("¡Despegue!");
        }
    }
}
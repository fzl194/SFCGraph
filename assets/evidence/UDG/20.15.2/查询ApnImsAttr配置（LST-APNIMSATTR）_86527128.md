# 查询ApnImsAttr配置（LST APNIMSATTR）

- [命令功能](#ZH-CN_CONCEPT_0186527128__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186527128__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186527128__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186527128__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186527128__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0186527128__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0186527128)

**适用NF：UPF**

命令用来查询APN的IMS属性信息。

#### [注意事项](#ZH-CN_CONCEPT_0186527128)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0186527128)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186527128)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186527128)

- 显示当前APN huawei.com的IMS属性信息：
  ```
  LST APNIMSATTR: APN="huawei.com";
  ```
  ```

  RETCODE = 0  操作成功。

  APN的IMS配置信息
  ----------------
           APN名称  =  huawei.com
           IMS开关  =  使能
  信令空口增强开关  =  使能
   (结果个数 = 1)
  ---    END
  ```
- 显示当前所有APN的IMS属性信息：
  ```
  LST APNIMSATTR:;
  ```
  ```

  RETCODE = 0  操作成功

  APN的IMS配置信息
  ----------------
  APN名称        IMS开关  

  testapn.com  使能         
  huawei.com     使能        
  (结果个数 = 2)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0186527128)

参见SET APNIMSATTR的参数说明。

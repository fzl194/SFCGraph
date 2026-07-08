# 查询用户模板的前缀URL组绑定关系（LST PREURLGBINDUP）

- [命令功能](#ZH-CN_CONCEPT_0182837413__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837413__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837413__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837413__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837413__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837413__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837413)

**适用NF：PGW-U、UPF**

该命令用于查询用户模板与前缀URL组的绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0182837413)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837413)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837413)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837413)

- 查询前缀URL组与名为testprofile的UserProfile的绑定关系：
  ```
  LST PREURLGBINDUP: USERPROFILENAME="testprofile";
  ```
  ```

  RETCODE = 0  操作成功。

  User Profile绑定Prefixed URL 组Information
  ------------------------------------------
  用户模板名称    前缀URL组名称

  testprofile     testurlgroup 
  testprofile     testurlgroup1
  (结果个数 = 2)
  ---    END
  ```
- 查询前缀URL组与UserProfile所有的绑定关系：
  ```
  LST PREURLGBINDUP:;
  ```
  ```

  RETCODE = 0  操作成功。

  User Profile绑定Prefixed URL 组Information
  ------------------------------------------
  用户模板名称    前缀URL组名称

  testprofile     testurlgroup 
  testprofile     testurlgroup1
  testprofile2    testurlgroup2
  (结果个数 = 3)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837413)

参见ADD PREURLGBINDUP的参数说明。

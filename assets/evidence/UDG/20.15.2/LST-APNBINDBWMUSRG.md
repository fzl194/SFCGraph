# 查询带宽管理用户组APN绑定（LST APNBINDBWMUSRG）

- [命令功能](#ZH-CN_CONCEPT_0182837489__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837489__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837489__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837489__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837489__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837489__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837489)

**适用NF：PGW-U、UPF**

该命令用于查询带宽管理用户组下绑定的APN。当运营商希望查询某用户组下绑定的APN，则执行该命令。

#### [注意事项](#ZH-CN_CONCEPT_0182837489)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837489)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837489)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPNAME | 用户组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要被APN绑定的带宽管理用户组名称，用户组名称由增加带宽管理用户组命令定义。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837489)

- 假如运营商希望查询名为“testbwmusergroup”的用户组下绑定的APN：
  ```
  LST APNBINDBWMUSRG:USERGROUPNAME="testbwmusergroup";
  ```
  ```

  RETCODE = 0  操作成功。

  用户组APN绑定信息
  -----------------
  用户组名称  =  testbwmusergroup
         APN  =  testapn
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商希望查询所有绑定APN的用户组：
  ```
  LST APNBINDBWMUSRG:;
  ```
  ```

  RETCODE = 0  操作成功。

  用户组APN绑定信息
  -----------------
  用户组名称          APN    

  testbwmusergroup    apn1   
  testbwmusergroup    testapn
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837489)

参见ADD APNBINDBWMUSRG的参数说明。

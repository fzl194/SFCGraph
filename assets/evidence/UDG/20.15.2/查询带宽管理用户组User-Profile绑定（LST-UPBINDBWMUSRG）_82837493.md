# 查询带宽管理用户组User Profile绑定（LST UPBINDBWMUSRG）

- [命令功能](#ZH-CN_CONCEPT_0182837493__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837493__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837493__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837493__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837493__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837493__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837493)

**适用NF：PGW-U、UPF**

该命令用于查询带宽管理用户组下绑定的UserProfile。当运营商希望查询某用户组下绑定的UserProfile信息，则执行该命令。

#### [注意事项](#ZH-CN_CONCEPT_0182837493)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837493)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837493)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPNAME | 用户组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要被用户模板绑定的带宽管理用户组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837493)

- 假如运营商希望查询名为“testbwmusergroup”的用户组下绑定的UserProfile：
  ```
  LST UPBINDBWMUSRG:USERGROUPNAME="testbwmusergroup";
  ```
  ```

  RETCODE = 0  操作成功。

  用户组User Profile绑定信息
  --------------------------
    用户组名称  =  testbwmusergroup
  用户模板名称  =  testuserprofile
  (结果个数 = 1)
  ---    END
  ```
- 假如运营商希望查询所有绑定UserProfile的用户组：
  ```
  LST UPBINDBWMUSRG:;
  ```
  ```

  RETCODE = 0  操作成功。

  用户组User Profile绑定信息
  --------------------------
  用户组名称          用户模板名称   

  testbwmusergroup    testuserprofile
  testbwmusergroup    userprofile    
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837493)

参见ADD UPBINDBWMUSRG的参数说明。

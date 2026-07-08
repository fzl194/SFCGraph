---
id: UDG@20.15.2@MMLCommand@LST UPBINDBWMUSRG
type: MMLCommand
name: LST UPBINDBWMUSRG（查询带宽管理用户组User Profile绑定）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPBINDBWMUSRG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理用户组用户模板绑定
status: active
---

# LST UPBINDBWMUSRG（查询带宽管理用户组User Profile绑定）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询带宽管理用户组下绑定的UserProfile。当运营商希望查询某用户组下绑定的UserProfile信息，则执行该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPNAME | 用户组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要被用户模板绑定的带宽管理用户组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPBINDBWMUSRG]] · 带宽管理用户组User Profile绑定（UPBINDBWMUSRG）

## 使用实例

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

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPBINDBWMUSRG.md`

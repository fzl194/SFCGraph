---
id: UDG@20.15.2@MMLCommand@LST APNBINDBWMUSRG
type: MMLCommand
name: LST APNBINDBWMUSRG（查询带宽管理用户组APN绑定）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNBINDBWMUSRG
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
- 带宽管理用户组APN绑定
status: active
---

# LST APNBINDBWMUSRG（查询带宽管理用户组APN绑定）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询带宽管理用户组下绑定的APN。当运营商希望查询某用户组下绑定的APN，则执行该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERGROUPNAME | 用户组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要被APN绑定的带宽管理用户组名称，用户组名称由增加带宽管理用户组命令定义。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNBINDBWMUSRG]] · 带宽管理用户组APN绑定（APNBINDBWMUSRG）

## 使用实例

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

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNBINDBWMUSRG.md`

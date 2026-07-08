---
id: UNC@20.15.2@MMLCommand@LST RULEBINDING
type: MMLCommand
name: LST RULEBINDING（查询用户模板和规则的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RULEBINDING
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 规则绑定
status: active
---

# LST RULEBINDING（查询用户模板和规则的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询规则与用户模板绑定关系。当运营商希望查询规则与用户模板绑定关系时，则执行该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户模板和规则的绑定关系（RULEBINDING）](configobject/UNC/20.15.2/RULEBINDING.md)

## 使用实例

- 假如运营商需要查询用户模板名称为userprofile的用户模板下绑定的规则：
  ```
  LST RULEBINDING: USERPROFILENAME="userprofile";
  ```
  ```

  RETCODE = 0  操作成功

  用户模板与规则绑定信息
  ----------------------
  用户模板名称  =  userprofile
      规则名称  =  testrule
      策略类型  =  PCC
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询所有的用户模板下绑定的规则：
  ```
  LST RULEBINDING:;
  ```
  ```

  RETCODE = 0  操作成功

  用户模板与规则绑定信息
  ----------------------
  用户模板名称  规则名称   策略类型  

  userprofile  testrule   PCC       
  up2           testrule2  PCC       
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户模板和规则的绑定关系（LST-RULEBINDING）_09897218.md`

---
id: UNC@20.15.2@MMLCommand@LST USRPROFGROUP
type: MMLCommand
name: LST USRPROFGROUP（查询用户模板组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRPROFGROUP
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
- 用户模板组
status: active
---

# LST USRPROFGROUP（查询用户模板组）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询UsrProfGroup。如果不输入UserProfGName，则查询系统中所有UsrProfGroup。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRPROFGROUP]] · 用户模板组（USRPROFGROUP）

## 使用实例

- 显示指定名称的UsrProfGroup配置：
  ```
  LST USRPROFGROUP:USERPROFGNAME="userprofg1";
  ```
  ```

  RETCODE = 0  操作成功。

  用户模板组信息
  --------------
   用户模板组名称  =  userprofg1
     用户模板数目  =  0
  用户PCC模板数目  =  0
  (结果个数 = 1)
  ---    END
  ```
- 显示所有UsrProfGroup配置：
  ```
  LST USRPROFGROUP:;
  ```
  ```

  RETCODE = 0  操作成功

  用户模板组信息
  --------------
  用户模板组名称  用户模板数目  用户PCC模板数目  

  userprofg1      0             0                
  userprofg2      0             0                
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-USRPROFGROUP.md`

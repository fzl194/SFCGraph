---
id: UDG@20.15.2@MMLCommand@LST FWPOLICY
type: MMLCommand
name: LST FWPOLICY（查询防火墙策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FWPOLICY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 防火墙策略控制
- 防火墙策略配置
status: active
---

# LST FWPOLICY（查询防火墙策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询所有防火墙策略，或者查询指定防火墙策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FWPOLICYNAME | 防火墙策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定防火墙策略的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [防火墙策略（FWPOLICY）](configobject/UDG/20.15.2/FWPOLICY.md)

## 使用实例

- 查询名为testfwpolicy的防火墙策略：
  ```
  LST FWPOLICY: FWPOLICYNAME="testfwpolicy";
  ```
  ```

  RETCODE = 0  操作成功。

  防火墙策略信息
  --------------
              防火墙策略名称  =  testfwpolicy
  上行发起业务流上行门控动作  =  Discard
  上行发起业务流下行门控动作  =  Discard
  下行发起业务流上行门控动作  =  Pass
  下行发起业务流下行门控动作  =  Pass
  (结果个数 = 1)

  ---    END
  ```
- 查询所有的防火墙策略：
  ```
  LST FWPOLICY:;
  ```
  ```

  RETCODE = 0  操作成功。

  防火墙策略信息
  --------------
  防火墙策略名称    上行发起业务流上行门控动作  上行发起业务流下行门控动作  下行发起业务流上行门控动作  下行发起业务流下行门控动作

  testfwpolicy      Discard                     Discard                      Pass                        Pass
  testfwpolicy1     Pass                        Pass                         Discard                     Discard
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询防火墙策略（LST-FWPOLICY）_70043022.md`

---
id: UDG@20.15.2@MMLCommand@RMV FWPOLICY
type: MMLCommand
name: RMV FWPOLICY（删除防火墙策略）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: FWPOLICY
command_category: 配置类
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

# RMV FWPOLICY（删除防火墙策略）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除所有防火墙策略，或者删除指定防火墙策略。

## 注意事项

- 该命令执行后立即生效。
- 如果防火墙策略被Rule绑定，删除时，需要将绑定关系解除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FWPOLICYNAME | 防火墙策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定防火墙策略的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FWPOLICY]] · 防火墙策略（FWPOLICY）

## 使用实例

- 删除名为testfwpolicy的防火墙策略：
  ```
  RMV FWPOLICY: FWPOLICYNAME="testfwpolicy";
  ```
- 删除所有的防火墙策略：
  ```
  RMV FWPOLICY:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-FWPOLICY.md`

---
id: UNC@20.15.2@MMLCommand@RTR ACLGROUP6
type: MMLCommand
name: RTR ACLGROUP6（清除IPv6 ACL规则匹配计数）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: ACLGROUP6
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- IPv6 ACL规则匹配计数
status: active
---

# RTR ACLGROUP6（清除IPv6 ACL规则匹配计数）

## 功能

该命令用于清除IPv6 ACL规则组下规则的匹配计数，也可以清除当前所有IPv6 ACL的匹配计数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | IPv6 ACL规则组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6 ACL规则属于哪个IPv6 ACL规则组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACLGROUP6]] · IPv6 ACL规则匹配计数（ACLGROUP6）

## 使用实例

- 用户需要清除当前所有IPv6 ACL规则的匹配计数：
  ```
  RTR ACLGROUP6:;
  ```
- 用户需要清除当前IPv6 ACL规则组2000的匹配计数：
  ```
  RTR ACLGROUP6:ACLNAME="2000";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除IPv6-ACL规则匹配计数（RTR-ACLGROUP6）_00440701.md`

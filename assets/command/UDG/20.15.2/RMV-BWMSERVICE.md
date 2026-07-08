---
id: UDG@20.15.2@MMLCommand@RMV BWMSERVICE
type: MMLCommand
name: RMV BWMSERVICE（删除带宽管理业务）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: BWMSERVICE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理业务
status: active
---

# RMV BWMSERVICE（删除带宽管理业务）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除带宽管理业务。当运营商希望删除已配置的带宽管理业务时，则执行该命令。

## 注意事项

- 该命令执行后立即生效。
- 如果带宽管理业务正在被引用，则不允许删除。
- 如果不指定带宽管理业务名称，则删除所有的带宽管理业务。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BWMSERVICENAME | 带宽控制业务名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置带宽管理业务的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BWMSERVICE]] · 带宽管理业务（BWMSERVICE）

## 使用实例

- 假如运营商需要删除名为“testbwmservice1”的带宽管理业务：
  ```
  RMV BWMSERVICE:BWMSERVICENAME="testbwmservice1";
  ```
- 假如运营商需要删除所有已配置的带宽管理业务：
  ```
  RMV BWMSERVICE:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除带宽管理业务（RMV-BWMSERVICE）_82837475.md`

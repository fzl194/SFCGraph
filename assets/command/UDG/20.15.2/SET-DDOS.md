---
id: UDG@20.15.2@MMLCommand@SET DDOS
type: MMLCommand
name: SET DDOS（设置DDoS防攻击流控阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DDOS
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- DDoS防护
- DDoS防护阈值
status: active
---

# SET DDOS（设置DDoS防攻击流控阈值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置DDoS攻击防护使用的流控阈值。DDoS攻击防护是通过对用户上行TCP SYN报文进行流控来实施的。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 使能该命令时，如果THRESHOLD参数配置过小，会影响用户新建流速率，建议使用默认值。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | THRESHOLD |
| --- | --- |
| 初始值 | 100 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| THRESHOLD | DDoS防护阈值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识单位时间内（固定1秒钟）允许通过的TCP SYN报文包数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10000。<br>默认值：无<br>配置原则：配置DDoS检查阈值后，用户在单位时间（1秒钟）内发起的TCP SYN请求个数不能超过此阈值，若超过此阈值，则会将超过的部分丢弃。 |

## 操作的配置对象

- [DDoS防攻击流控阈值（DDOS）](configobject/UDG/20.15.2/DDOS.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00084]]

## 使用实例

- 假设运营商需要对用户的上行TCP SYN报文进行流控处理，通过配置SET DDOS命令来实现，Threshold为5000：
  ```
  SET DDOS:THRESHOLD=5000;
  ```
- 通过配置DDoS的值为100恢复到系统的缺省值，Threshold为100：
  ```
  SET DDOS:THRESHOLD=100;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置DDoS防攻击流控阈值（SET-DDOS）_82837754.md`

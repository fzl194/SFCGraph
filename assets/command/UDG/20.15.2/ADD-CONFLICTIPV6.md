---
id: UDG@20.15.2@MMLCommand@ADD CONFLICTIPV6
type: MMLCommand
name: ADD CONFLICTIPV6（添加本地地址池中冲突IPv6地址）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CONFLICTIPV6
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 10000
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 冲突地址管理
- IPv6冲突地址管理
status: active
---

# ADD CONFLICTIPV6（添加本地地址池中冲突IPv6地址）

## 功能

**适用NF：UPF**

该命令用于在本地地址池中标识指定IPv6地址为冲突状态。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- 如果要限制本地地址池中的某个地址不能分配给终端用户，比如这个地址与系统或其他设备本身的地址冲突，可以使用ADD CONFLICTIPV6命令标识相应地址为冲突状态，禁止设备地址被分配给终端用户。
- 配置冲突IP地址前，需要先执行ADD POOL命令配置地址池。
- 如果某地址已经分配给终端用户，此时通过命令配置该地址为冲突地址，命令依然可以执行成功，但是配置生效是在下次分配该地址的时候。
- 配置为冲突状态的IP不会分配给用户，该地址池可用地址数减少。
- 一个地址池最多可以设置16个地址为冲突状态。
- 冲突地址的前缀长度和对应地址池下的地址段前缀长度相同时，冲突地址才生效。
- 同一地址池下添加的冲突prefix不允许重叠。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| V6PREFIX | 冲突IPv6地址前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定冲突IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。冒号分十六进制，格式为X:X:X:X:X:X:X:X。除了组播地址、链路本地地址、环回地址或未指定的地址为非法地址外，其他都为合法地址。<br>默认值：无<br>配置原则：无 |
| V6PREFIXLENGTH | IPv6前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定冲突IPv6地址的前缀长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为49～64。配置范围49-64。<br>默认值：64<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CONFLICTIPV6]] · 本地地址池中冲突IPv6地址（CONFLICTIPV6）

## 使用实例

在本地地址池lap指定一个冲突地址，POOLNAME为“lap”，V6PREFIX为"fc01:0000:0000:0000:0000:0000:0000:0001"，V6PREFIXLENGTH为64：

```
ADD CONFLICTIPV6: POOLNAME="lap", V6PREFIX="fc01:0000:0000:0000:0000:0000:0000:0001", V6PREFIXLENGTH=64;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-CONFLICTIPV6.md`

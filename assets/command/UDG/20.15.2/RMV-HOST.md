---
id: UDG@20.15.2@MMLCommand@RMV HOST
type: MMLCommand
name: RMV HOST（删除Host）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HOST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 主机名
status: active
---

# RMV HOST（删除Host）

## 功能

**适用NF：PGW-U、UPF**

RMV HOST此命令用来删除指定Host主机名或所有Host主机名。

## 注意事项

- 该命令执行后立即生效。
- 在删除Host信息执行RMV HOST命令前，需要确定HostName是否被Filter对象引用，如已绑定需先解除绑定后执行RMV HOST命令。
- 输入HostName删除指定配置。不输入HostName进行删除，执行一次删除命令最多删除5000条配置。
- 通过 ADD FILTER 或 MOD FILTER 中的参数Host配置名称可以解绑Host，最后一个解绑的Host生效时间为60s，其他解绑立刻生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | Host配置名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HOST配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HOST]] · Host（HOST）

## 使用实例

删除Host主机名称，主机名为“huawei”：

```
RMV HOST:HOSTNAME="huawei";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Host（RMV-HOST）_86528750.md`

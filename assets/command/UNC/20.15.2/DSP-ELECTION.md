---
id: UNC@20.15.2@MMLCommand@DSP ELECTION
type: MMLCommand
name: DSP ELECTION（显示集群选举实例信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ELECTION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP ELECTION（显示集群选举实例信息）

## 功能

此命令用于查询集群选举实例的信息，竞选实例组成集群，从中选出主和备。

## 注意事项

手动复位hafetcd服务的主时，至少延迟10秒再使用该命令查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ELECTION]] · 集群选举实例信息（ELECTION）

## 使用实例

获取集群选举实例的位置信息、主从信息、服务状态等：

```
%%DSP ELECTION:;%%
RETCODE = 0  操作成功
 
结果如下
------------------------
节点标识      Pod名称            ETCD实例标识       IP地址/端口号          角色      运行状态       开源版本号       数据存储量       递交时延

192.168.0.1  hafetcd-pod-2     b35a5665f835ac8c  192.168.1.54:2379     主节点     正常          3.3.6           332 kB          1.925483ms
192.168.0.2  hafetcd-pod-0     b10a1908d6d9f545  192.168.1.48:2379     从节点     正常          3.3.6           332 kB          12.376402ms
192.168.0.3  hafetcd-pod-1     675b998e579d3b37  192.168.1.51:2379     从节点     正常          3.3.6           332 kB          3.204205ms
(结果个数 = 3)
 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ELECTION.md`

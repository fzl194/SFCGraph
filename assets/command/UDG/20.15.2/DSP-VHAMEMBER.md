---
id: UDG@20.15.2@MMLCommand@DSP VHAMEMBER
type: MMLCommand
name: DSP VHAMEMBER（查询vHA ETCD集群节点详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: VHAMEMBER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP VHAMEMBER（查询vHA ETCD集群节点详细信息）

## 功能

该命令用于查询vHA ETCD集群节点的详细信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/VHAMEMBER]] · vHA ETCD集群节点详细信息（VHAMEMBER）

## 使用实例

查询集群节点相关信息：

```
%%DSP VHAMEMBER:;%%
RETCODE = 0  操作成功

结果如下
------------------------
节点名称    与Client通讯地址              与Peer通讯地址                      节点成员标识        角色    运行状态     Pod名称     Node名称     版本号     存储数据大小  集群节点个数

vha-pod-1  https://192.168.0.111:32199  https://vha-pod-1.vha.fenix:32198  ad119e2976360a39  从节点  健康         vha-pod-1  192.168.0.1  3.4.60604  1.9MB      3
vha-pod-2  https://192.168.0.222:32199  https://vha-pod-2.vha.fenix:32198  c9c24b5a9a36dd45  主节点  健康         vha-pod-2  192.168.0.2  3.4.60604  1.9MB      3
vha-pod-0  https://192.168.0.333:32199  https://vha-pod-0.vha.fenix:32198  c27db378e0a584b9  从节点  健康         vha-pod-0  192.168.0.3  3.4.60604  1.9MB      3
(Number of results = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询vHA-ETCD集群节点详细信息（DSP-VHAMEMBER）_51852642.md`

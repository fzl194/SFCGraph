---
id: UNC@20.15.2@MMLCommand@LST PNFUPFINFO
type: MMLCommand
name: LST PNFUPFINFO（查询对端UPF信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFUPFINFO
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF UPF信息管理
status: active
---

# LST PNFUPFINFO（查询对端UPF信息）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询本地配置的对端UPF实例的相关信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFUPFINFO]] · 对端UPF信息（PNFUPFINFO）

## 使用实例

查询本地配置的对端UPF支持的信息。

```
%%LST PNFUPFINFO:;%%
RETCODE = 0 操作成功

结果如下：
------------------------
            NF实例标识 = upf_instance_0
UPF是否支持与EPS的互通 = TRUE
           PDU会话类型 = IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFUPFINFO.md`

---
id: UNC@20.15.2@MMLCommand@LST PNFPLMNRANGE
type: MMLCommand
name: LST PNFPLMNRANGE（查询对端NF的PLMN范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFPLMNRANGE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例PLMN范围管理
status: active
---

# LST PNFPLMNRANGE（查询对端NF的PLMN范围）

## 功能

**适用NF：AMF、SMF、NSSF、NCG**

该命令用于查询本地的配置对端NF实例支持的PLMN范围信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFPLMNRANGE]] · 对端NF的PLMN范围（PNFPLMNRANGE）

## 使用实例

查询对端NF的PLMN范围信息。

```
%%LST PNFPLMNRANGE:;%%
RETCODE = 0 操作成功

结果如下
------------------------
        索引 = 1
  NF实例标识 = chf_instance_0
    查询方式 = START_END
    起始号段 = 12300
    终止号段 = 12303
        模式 = NULL
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFPLMNRANGE.md`

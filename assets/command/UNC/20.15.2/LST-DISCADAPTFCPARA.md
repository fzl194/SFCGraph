---
id: UNC@20.15.2@MMLCommand@LST DISCADAPTFCPARA
type: MMLCommand
name: LST DISCADAPTFCPARA（查询服务发现自适应流控全局配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DISCADAPTFCPARA
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 服务发现自适应流控
status: active
---

# LST DISCADAPTFCPARA（查询服务发现自适应流控全局配置）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询服务发现自适应流控全局配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DISCADAPTFCPARA]] · 服务发现自适应流控全局配置（DISCADAPTFCPARA）

## 使用实例

查询服务发现自适应流控全局配置

```
%%LST DISCADAPTFCPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
自适应流控NRF返回码  =  429-503-504-604-605
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DISCADAPTFCPARA.md`

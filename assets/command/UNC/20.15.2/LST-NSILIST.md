---
id: UNC@20.15.2@MMLCommand@LST NSILIST
type: MMLCommand
name: LST NSILIST（查询NF支持切片信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSILIST
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 网络切片实例列表管理
status: active
---

# LST NSILIST（查询NF支持切片信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG**

该命令用于查询NF实例支持的网络切片实例标识。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSILIST]] · NF支持切片信息（NSILIST）

## 使用实例

运营商A需要查询NF实例支持的网络切片实例标识。

```
%%LST NSILIST:;%%
RETCODE = 0  操作成功

结果如下
--------
      NF实例名称  =  AMF_Instance_0
网络切片实例标识  =  NS_Instance_0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSILIST.md`

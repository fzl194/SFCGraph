---
id: UNC@20.15.2@MMLCommand@LST SLICEINSTINFO
type: MMLCommand
name: LST SLICEINSTINFO（查询服务支持的切片实例）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SLICEINSTINFO
command_category: 查询类
applicable_nf:
- SMF
- AMF
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
- 服务支持的切片实例管理
status: active
---

# LST SLICEINSTINFO（查询服务支持的切片实例）

## 功能

**适用NF：SMF、AMF、NRF、NSSF、NCG**

该命令用于查询切片实例管理。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SLICEINSTINFO]] · 服务支持的切片实例（SLICEINSTINFO）

## 使用实例

查询所有的切片实例管理：

```
%%LST SLICEINSTINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
    网络分片实例信息  =  1
网络分片子网实例标识  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SLICEINSTINFO.md`

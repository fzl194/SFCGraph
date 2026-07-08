---
id: UNC@20.15.2@MMLCommand@LST IMSIBINDUPFADDR
type: MMLCommand
name: LST IMSIBINDUPFADDR（查询用户和UPF的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIBINDUPFADDR
command_category: 查询类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- PFCP路径选择管理
status: active
---

# LST IMSIBINDUPFADDR（查询用户和UPF的绑定关系）

## 功能

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于查询用户和UPF的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIBINDUPFADDR]] · 用户和UPF地址的绑定关系（IMSIBINDUPFADDR）

## 使用实例

查询所有用户的UPF地址绑定关系：

```
%%LST IMSIBINDUPFADDR:;%%
RETCODE = 0  操作成功。

结果如下
------------------------
   起始IMSI  =  111111000000000
   终止IMSI  =  111111999999999
UPF实例标识  =  up1
     IP类型  =  IPV4
   IPv4地址  =  10.0.0.2  
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMSIBINDUPFADDR.md`

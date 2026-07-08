---
id: UNC@20.15.2@MMLCommand@DSP NGM2MUSERNUM
type: MMLCommand
name: DSP NGM2MUSERNUM（显示5G M2M用户资源数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGM2MUSERNUM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# DSP NGM2MUSERNUM（显示5G M2M用户资源数）

## 功能

**适用NF：AMF**

该命令用于查询AMF系统内M2M用户资源的统计结果。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGM2MUSERNUM]] · 5G M2M用户资源数（NGM2MUSERNUM）

## 使用实例

查看AMF上的M2M用户资源统计结果，执行如下命令：

```
%%DSP NGM2MUSERNUM:;%%
RETCODE = 0  操作成功

结果如下
------------------------
5G RedCap注册态用户数  5G RedCap PDU会话数  POD ID    

10                     12                   usn-pod-0 0  
10                     12                   total            
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示5G-M2M用户资源数（DSP-NGM2MUSERNUM）_78121270.md`

---
id: UDG@20.15.2@MMLCommand@DSP LICENSERES
type: MMLCommand
name: DSP LICENSERES（显示License资源）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LICENSERES
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# DSP LICENSERES（显示License资源）

## 功能

该命令用于查看License资源数目以及使用情况。

> **说明**
> - 系统中使用的用户数资源，指的是系统在线用户数的使用数目。
> - 该命令执行后立即生效。
> - 当License文件未激活时，查询结果为空，激活后只能查询购买量不等于0且支持显示的资源项。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [License资源（LICENSERES）](configobject/UDG/20.15.2/LICENSERES.md)

## 使用实例

查询License资源：

```
%%DSP LICENSERES:;%%
RETCODE = 0  操作成功

操作结果如下
------------
资源项         资源名称                              资源总数    已使用资源    使用率
LKV7RIPV601    支持用户面IPv6 PDP（每千PDP/承载）    12000       0             0%    
LKV7CDRS01     每秒话单数（CDR/秒）                  32000       0             0%    
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示License资源（DSP-LICENSERES）_09587935.md`

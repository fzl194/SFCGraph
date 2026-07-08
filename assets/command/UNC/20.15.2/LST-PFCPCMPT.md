---
id: UNC@20.15.2@MMLCommand@LST PFCPCMPT
type: MMLCommand
name: LST PFCPCMPT（查询PFCP接口兼容性参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PFCPCMPT
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP接口兼容性
status: active
---

# LST PFCPCMPT（查询PFCP接口兼容性参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询PFCP接口兼容性参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PFCPCMPT]] · PFCP接口兼容性参数（PFCPCMPT）

## 使用实例

查询PFCP接口兼容性配置，执行如下命令：

```
%%LST PFCPCMPT:;%%
RETCODE = 0  操作成功

结果如下
--------
     是否支持BAR信元  =  不支持
是否携带地址池占位符  =   否
         是否填写VPN  =   否
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PFCPCMPT.md`

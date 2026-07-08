---
id: UNC@20.15.2@MMLCommand@DSP GENERATECDR
type: MMLCommand
name: DSP GENERATECDR（查询强制生成话单结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GENERATECDR
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费维护
- 强制生成话单结果查询
status: active
---

# DSP GENERATECDR（查询强制生成话单结果）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查询上次强制产生用户话单结果信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GENERATECDR]] · 立即生成话单（GENERATECDR）

## 使用实例

查询上次强制产生所有用户话单信息：

```
DSP GenerateCDR:;
```

```

RETCODE = 0 操作成功

上次强制话单生成结果
-------------------------
                    POD名称  =  uncpod-012-30-0-243__1020__0
                       时间  =  2015-08-21 14:17:47
                 成功话单数  =  1
                 失败话单数  =  0
                     结果  =  成功
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GENERATECDR.md`

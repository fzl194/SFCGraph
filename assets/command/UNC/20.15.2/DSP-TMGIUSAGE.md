---
id: UNC@20.15.2@MMLCommand@DSP TMGIUSAGE
type: MMLCommand
name: DSP TMGIUSAGE（显示TMGI使用率）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TMGIUSAGE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- MB-SMF组播广播管理
- 显示MB-SMF TMGI使用率
status: active
---

# DSP TMGIUSAGE（显示TMGI使用率）

## 功能

**适用NF：SMF**

该命令用于显示TMGI使用率。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [TMGI使用率（TMGIUSAGE）](configobject/UNC/20.15.2/TMGIUSAGE.md)

## 使用实例

当需要显示TMGI使用率时，执行如下命令：

```
%%DSP TMGIUSAGE:;%%
RETCODE = 0  操作成功

结果如下
--------
已分配的TMGI数量  =  0
        TMGI总数  =  2
      TMGI使用率  =  0.00%
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示TMGI使用率（DSP-TMGIUSAGE）_97301786.md`

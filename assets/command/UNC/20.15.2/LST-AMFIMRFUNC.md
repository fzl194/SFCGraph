---
id: UNC@20.15.2@MMLCommand@LST AMFIMRFUNC
type: MMLCommand
name: LST AMFIMRFUNC（查询用户消息统计功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFIMRFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 信令采集
status: active
---

# LST AMFIMRFUNC（查询用户消息统计功能配置）

## 功能

**适用NF：AMF**

该命令用于查询用户消息统计功能配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFIMRFUNC]] · 用户消息统计功能配置（AMFIMRFUNC）

## 使用实例

查询所有的AMFIMRFUNC记录：

```
%%LST AMFIMRFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
用户范围  =  所有用户
接口类型  =  Nas
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户消息统计功能配置（LST-AMFIMRFUNC）_44006790.md`

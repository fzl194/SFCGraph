---
id: UDG@20.15.2@MMLCommand@LST CERTUPDATPARA
type: MMLCommand
name: LST CERTUPDATPARA（查询证书更新流程参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CERTUPDATPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS证书更新流程参数管理
status: active
---

# LST CERTUPDATPARA（查询证书更新流程参数）

## 功能

该命令用于查询证书更新流程参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CERTUPDATPARA]] · 证书更新流程参数（CERTUPDATPARA）

## 使用实例

查询证书更新流程参数，可以用如下命令：

```
%%LST CERTUPDATPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------
               单进程每批次重建链路间隔(s)  =  4
                    单进程每批次重建链路数  =  10
                  证书更新时是否重建旧链路  =  TRUE
单证书场景单进程客户端链路允许不更新的数量  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CERTUPDATPARA.md`

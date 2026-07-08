---
id: UNC@20.15.2@MMLCommand@LST HTTPERRHANDLER
type: MMLCommand
name: LST HTTPERRHANDLER（查询间接路由代理故障重选配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPERRHANDLER
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- 间接路由代理故障处理
status: active
---

# LST HTTPERRHANDLER（查询间接路由代理故障重选配置）

## 功能

**适用NF：SMF**

该命令用于查询间接路由代理故障重选配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HTTPERRHANDLER]] · 间接路由代理故障重选配置（HTTPERRHANDLER）

## 使用实例

查询间接路由代理故障重选配置。

```
%%LST HTTPERRHANDLER:;%%
RETCODE = 0  操作成功
结果如下
--------
            对端网络功能类型  =  UDM
                      状态码  =  500
     间接路由代理故障处理开关 = 使能
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HTTPERRHANDLER.md`

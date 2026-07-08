---
id: UNC@20.15.2@MMLCommand@LST HTTPSRVLBSW
type: MMLCommand
name: LST HTTPSRVLBSW（查询HTTP服务端负载重均衡功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPSRVLBSW
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP服务端负载管理
- POD内负载管理
status: active
---

# LST HTTPSRVLBSW（查询HTTP服务端负载重均衡功能）

## 功能

该命令用于查询HTTP服务端负载重均衡功能参数的配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPSRVLBSW]] · HTTP服务端负载重均衡功能（HTTPSRVLBSW）

## 使用实例

用户查询服务端负载重均衡开关、监控参数以及服务端重均衡负载的门限，执行如下命令：

```
%%LST HTTPSRVLBSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
          服务端负载均衡功能开关  =  关闭
		   服务端重均衡偏差门限  =  10
            服务端重均衡最大门限  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-HTTPSRVLBSW.md`

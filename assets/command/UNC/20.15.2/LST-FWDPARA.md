---
id: UNC@20.15.2@MMLCommand@LST FWDPARA
type: MMLCommand
name: LST FWDPARA（查询转发参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FWDPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 系统参数
status: active
---

# LST FWDPARA（查询转发参数）

## 功能

该命令用于查询转发参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/FWDPARA]] · 转发参数（FWDPARA）

## 使用实例

查询转发参数。

LST FWDPARA:;

```
%%LST FWDPARA:;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
    报文重组超时时长（秒）  =  6
IPv6报文重组超时时长（秒）  =  6
          分片报文转板开关  =  开
                批量收包数  =  128
              批量收包次数  =  4
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询转发参数（LST-FWDPARA）_29627124.md`

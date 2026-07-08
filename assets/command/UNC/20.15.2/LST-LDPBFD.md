---
id: UNC@20.15.2@MMLCommand@LST LDPBFD
type: MMLCommand
name: LST LDPBFD（查询LDP BFD配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LDPBFD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP BFD管理
status: active
---

# LST LDPBFD（查询LDP BFD配置）

## 功能

该命令用于查询LDP BFD配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/LDPBFD]] · LDP BFD配置（LDPBFD）

## 使用实例

查询LDP BFD配置：

```
LST LDPBFD:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                                  LDP BFD能力  =  TRUE
                   BFD For LDP Tunnel触发策略  =  主机
               BFD For LDP Tunnel的IP前缀名称  =  NULL
               BFD For LDP Tunnel FEC列表名称  =  NULL
BFD For LDP Tunnel的BFD最小发送时间间隔（ms）  =  45
BFD For LDP Tunnel的BFD最小接收时间间隔（ms）  =  45
        BFD For LDP Tunnel的BFD可容忍丢失次数  =  40
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询LDP-BFD配置（LST-LDPBFD）_50281682.md`

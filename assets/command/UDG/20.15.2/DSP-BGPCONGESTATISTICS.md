---
id: UDG@20.15.2@MMLCommand@DSP BGPCONGESTATISTICS
type: MMLCommand
name: DSP BGPCONGESTATISTICS（查询BGP流控信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BGPCONGESTATISTICS
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP流控信息
status: active
---

# DSP BGPCONGESTATISTICS（查询BGP流控信息）

## 功能

该命令可以查看当前系统中BGP中各个组件的流控计数信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPTYPE | 组件类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定组件类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BGP_NM：BNM组件。<br>- BGP_RM_IPV4：BRM IPv4组件。<br>- BGP_RM_IPV6：BRM IPv6组件。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BGPCONGESTATISTICS]] · BGP流控信息（BGPCONGESTATISTICS）

## 使用实例

查询BGP流控信息：

```
DSP BGPCONGESTATISTICS:COMPTYPE=BGP_NM;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
        组件类型  =  BGP_NM
          进程ID  =  10001
         组件PID  =  1245251
  Partner组件PID  =  2148794507
 Partner组件类型  =  20
        流控计数  =  0
    解除流控计数  =  0
    上次流控时间  =  NULL
上次解除流控时间  =  NULL
    当前流控状态  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-BGPCONGESTATISTICS.md`

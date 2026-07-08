---
id: UNC@20.15.2@MMLCommand@DSP BGPASMSG
type: MMLCommand
name: DSP BGPASMSG（查询BGP AS查询消息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BGPASMSG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP AS号消息
status: active
---

# DSP BGPASMSG（查询BGP AS查询消息）

## 功能

该命令用来查询BGP AS查询消息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/BGPASMSG]] · BGP AS查询消息（BGPASMSG）

## 使用实例

查询BGP AS查询消息：

```
DSP BGPASMSG:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
VPN名称        =  vrf1
 返回码        =  1
原始AS号       =  200
查询时间       =  2016-12-12T03:46:40
查询模式       =  2
目的地址       =  192.168.3.1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BGP-AS查询消息（DSP-BGPASMSG）_49961022.md`

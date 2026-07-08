---
id: UNC@20.15.2@MMLCommand@DSP RAWLINKSTATISTIC
type: MMLCommand
name: DSP RAWLINKSTATISTIC（查询Raw-link报文统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RAWLINKSTATISTIC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- Raw-link报文统计
status: active
---

# DSP RAWLINKSTATISTIC（查询Raw-link报文统计）

## 功能

该命令用于查看Raw-link连接的报文统计信息。

Raw-link连接的流量统计信息主要分为发送和接收两大部分。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/RAWLINKSTATISTIC]] · Raw-link报文统计（RAWLINKSTATISTIC）

## 使用实例

显示当前系统的Raw-link报文统计：

```
DSP RAWLINKSTATISTIC:;
```

```

        RETCODE = 0  操作成功

        结果如下
        ------------------------
                       接收报文计数  =  0
        接收报文PCB缓存查询失败计数  =  0
                       发送报文计数  =  0
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Raw-link报文统计（DSP-RAWLINKSTATISTIC）_00840985.md`

---
id: UDG@20.15.2@MMLCommand@LST RTSDNNPARA
type: MMLCommand
name: LST RTSDNNPARA（显示RTSDNN参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RTSDNNPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- RTSDNN业务控制
- RTSDNN参数
status: active
---

# LST RTSDNNPARA（显示RTSDNN参数）

## 功能

**适用NF：PGW-U、UPF**

查询通用DNN漫游分流参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/RTSDNNPARA]] · RTSDNN参数（RTSDNNPARA）

## 使用实例

使用LST RTSDNNPARA命令查询通用DNN漫游分流参数：

```
LST RTSDNNPARA:;
```

```

RETCODE = 0  Operation succeeded

RTSDNN Parameter
-----------------
                                       Public Network Switch  =  DISABLE
                                      Private Network Switch  =  DISABLE
                                       IPv4 NAT ALG Protocol  =  FTP Protocol&RTSP Protocol
                                       IPv6 NAT ALG Protocol  =  FTP Protocol
              Flow Control Interval for MultiDNN Reports (s)  =  2
                                         Actions for Packets  =  Discard
                     UE IP Address Conflict Detection Switch  =  ENABLE
                           UE IP Address Reallocation Switch  =  ENABLE
                Maximum Number of UE IP Address Reassignment  =  1000
                   Handling Policy on UE IP Address Conflict  =  BYPASS
            Check Interval for the Campus Resource Threshold  =  240
General DNN-based Roaming Traffic Steering Reporting over N4  =  ENABLE
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RTSDNNPARA.md`

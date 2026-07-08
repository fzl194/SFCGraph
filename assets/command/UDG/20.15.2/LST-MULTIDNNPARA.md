---
id: UDG@20.15.2@MMLCommand@LST MULTIDNNPARA
type: MMLCommand
name: LST MULTIDNNPARA（显示MultiDNN参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MULTIDNNPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- MultiDNN业务控制
- MultiDNN参数
status: active
---

# LST MULTIDNNPARA（显示MultiDNN参数）

## 功能

**适用NF：PGW-U、UPF**

查询MultiDNN参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/MULTIDNNPARA]] · MultiDNN参数（MULTIDNNPARA）

## 使用实例

使用LST MULTIDNNPARA命令查询MultiDNN参数：

```
LST MULTIDNNPARA:;
```

```

RETCODE = 0  Operation succeeded

MultiDNN Parameter
------------------
                        MultiDNN Function Switch  =  ENABLE
                           IPv4 NAT ALG Protocol  =  FTP Protocol&RTSP Protocol
                           IPv6 NAT ALG Protocol  =  FTP Protocol
           Flow Control Interval for Reports (s)  =  2
                             Actions for Packets  =  Discard
                    UE IP Address Conflict Check  =  ENABLE
                       UE IP Reallocation Switch  =  ENABLE
            Number of UE IP Address Reallocation  =  1000
     Policy for Handling UE IP Address Conflicts  =  BYPASS
Check Interval for the Campus Resource Threshold  =  240
                       N4 Report MultiDNN Switch  =  ENABLE
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示MultiDNN参数（LST-MULTIDNNPARA）_70853530.md`

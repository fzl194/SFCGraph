---
id: UDG@20.15.2@MMLCommand@DSP CUINCONSCONFIG
type: MMLCommand
name: DSP CUINCONSCONFIG（显示CP和UP不一致的关键配置）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CUINCONSCONFIG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 配置校验控制
- CP和UP不一致的关键配置
status: active
---

# DSP CUINCONSCONFIG（显示CP和UP不一致的关键配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查看当前影响系统的SMF/PGW-C和UPF/PGW-U不一致的部分配置。

## 注意事项

当SMF/PGW-C发送的消息中携带多个UPF/PGW-U未配置的Service Property信元时，DSP CUINCONSCONFIG命令仅显示第一个未配置的Service Property信元。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [CP和UP不一致的关键配置（CUINCONSCONFIG）](configobject/UDG/20.15.2/CUINCONSCONFIG.md)

## 使用实例

查询SMF/PGW-C和UPF/PGW-U不一致的配置：

```
DSP CUINCONSCONFIG:;
```

```

RETCODE = 0  操作成功

CP和UP不一致的配置
---------------------------------------
Result  =  
No    CP Node ID Type    CP Node ID Value    IE/Cfg Type         Cause                        IE/Cfg Name
1     IPV4               192.168.10.10       Common Policy       Unknown_IE_Name              test 
2     IPV4               192.168.10.10       Predefined Rule     Unknown_IE_Name              11116667
3     IPV4               192.168.10.10       Service Property    Unknown_IE_Name              sp_1   
4     IPV4               192.168.10.10       Service Property    Exceeded_Specifications             
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示CP和UP不一致的关键配置（DSP-CUINCONSCONFIG）_72134994.md`

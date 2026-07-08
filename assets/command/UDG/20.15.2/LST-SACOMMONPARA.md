---
id: UDG@20.15.2@MMLCommand@LST SACOMMONPARA
type: MMLCommand
name: LST SACOMMONPARA（查询SA业务公共参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SACOMMONPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- SA公共参数
status: active
---

# LST SACOMMONPARA（查询SA业务公共参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示SA业务相关控制参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SACOMMONPARA]] · SA业务公共参数（SACOMMONPARA）

## 使用实例

显示SA业务相关控制参数：

```
LST SACOMMONPARA:;
```

```

RETCODE = 0 操作成功。

SA业务公共参数信息
------------------
没有确定业务的报文的个数 = 0
               CDN增强识别功能  = 不使能
Quic SA协议确定后进行匹配的开关 = 不使能
           用户关联识别刷新开关 = 不使能
           Quic协议识别功能增强 = 不使能
           Quic协议解析功能增强 = 不使能
           HTTP特殊方法解析开关 = 使能
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SA业务公共参数（LST-SACOMMONPARA）_82837415.md`

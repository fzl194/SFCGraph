---
id: UDG@20.15.2@MMLCommand@LST RELAYURLAUTH
type: MMLCommand
name: LST RELAYURLAUTH（查询媒体中继URL鉴权配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYURLAUTH
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继URL鉴权
status: active
---

# LST RELAYURLAUTH（查询媒体中继URL鉴权配置）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询媒体中继URL鉴权配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYURLAUTHNM | 媒体中继URL鉴权名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定媒体中继URL鉴权名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [媒体中继URL鉴权配置（RELAYURLAUTH）](configobject/UDG/20.15.2/RELAYURLAUTH.md)

## 使用实例

查询媒体中继URL鉴权配置：

```
LST RELAYURLAUTH:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
 媒体中继URL鉴权名称  =  urlauth
 媒体中继鉴权密钥名称  =  auth1
        URL鉴权方法  =  鉴权方式B
           加密算法  =  SHA256
           有效时间  =  1440
         时间戳格式  =  日期
       鉴权失败动作  =  禁止访问（403）
       鉴权字段名称  =  NULL
      时间戳字段名称  =  NULL
	Dash扩展鉴权开关 =  不使能
         配置域名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询媒体中继URL鉴权配置（LST-RELAYURLAUTH）_43992598.md`

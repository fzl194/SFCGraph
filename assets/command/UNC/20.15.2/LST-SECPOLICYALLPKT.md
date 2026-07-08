---
id: UNC@20.15.2@MMLCommand@LST SECPOLICYALLPKT
type: MMLCommand
name: LST SECPOLICYALLPKT（查询上送报文总体速率）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SECPOLICYALLPKT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略总报文
status: active
---

# LST SECPOLICYALLPKT（查询上送报文总体速率）

## 功能

该命令用来查询上送报文总体速率设置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：可选参数<br>参数含义：策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |

## 操作的配置对象

- [上送报文总体速率（SECPOLICYALLPKT）](configobject/UNC/20.15.2/SECPOLICYALLPKT.md)

## 使用实例

查询上送报文总体速率设置：

```
LST SECPOLICYALLPKT:SECPOLICYID=1;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  安全策略编号    =  1
上报速率值（pps） =  6000
  上报速率等级    =  高
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询上送报文总体速率（LST-SECPOLICYALLPKT）_49961738.md`

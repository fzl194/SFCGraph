---
id: UNC@20.15.2@MMLCommand@LST HPLMN
type: MMLCommand
name: LST HPLMN（查询本地PLMN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HPLMN
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MNO管理
- MNO网络配置表
status: active
---

# LST HPLMN（查询本地PLMN）

## 功能

**适用网元：SGSN、MME**

此命令用于查看归属PLMN配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：待查询HPLMN的移动国家号码。<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：待查询HPLMN的移动网号码。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |

## 操作的配置对象

- [本地PLMN（HPLMN）](configobject/UNC/20.15.2/HPLMN.md)

## 使用实例

查看所有HPLMN：

LST HPLMN:;

```
%%LST HPLMN:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
            移动国家码  =  460
              移动网号  =  03
                国家码  =  086
               MNO标识  =  128
        是否允许SM业务  =  允许
            最大承载数  =  11
       是否允许SMS业务  =  允许
是否允许纠正短消息中心  =  不允许
    纠正后的短消息中心  =  NULL
       是否允许LCS业务  =  允许
              协议类型  =  GTP
            运营商名称  =  noname
  是否允许紧急呼叫业务  =  允许
      紧急号码下发开关  =  开启
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本地PLMN(LST-HPLMN)_72345675.md`

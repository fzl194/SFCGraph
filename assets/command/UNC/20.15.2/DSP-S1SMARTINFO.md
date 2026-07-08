---
id: UNC@20.15.2@MMLCommand@DSP S1SMARTINFO
type: MMLCommand
name: DSP S1SMARTINFO（显示S1模式用户信令状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: S1SMARTINFO
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 异常信令节省
- S1模式信令抑制维护
status: active
---

# DSP S1SMARTINFO（显示S1模式用户信令状态）

## 功能

**适用网元：MME**

该命令用于查询S1模式下的用户信令状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令查询的请求次数显示为当前统计周期内的请求次数，统计周期为1小时。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的国际移动用户标识。<br>是否必选：必选<br>数据来源：本端规划<br>取值范围：1～15位十进制数字字符串。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1SMARTINFO]] · S1模式用户信令状态（S1SMARTINFO）

## 使用实例

查询IMSI为123036500000002的用户的S1模式信令状态：

DSP S1SMARTINFO: IMSI="123036500000002";

```
%%DSP S1SMARTINFO: IMSI="123036500000002";%%
RETCODE = 0  操作成功。
用户信息
-----------------
            IMSI  =  123036500000002
        终端类型  =  iOS
    附着抑制类型  =  未被抑制
    附着请求次数  =  1
服务请求抑制类型  =  未被抑制
    服务请求次数  =  0
         APN个数  =  2
(结果个数 = 1)
Apn信息:
----------------
 APN标识          PDN连接抑制类型           PDN连接请求次数
 HUAWEI3.COM     Reject with a Specific Cause   2                                  
 HUAWEI1.COM     Reject with a Specific Cause   2                                  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-S1SMARTINFO.md`

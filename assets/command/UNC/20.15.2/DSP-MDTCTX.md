---
id: UNC@20.15.2@MMLCommand@DSP MDTCTX
type: MMLCommand
name: DSP MDTCTX（显示MDT上下文）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MDTCTX
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
- MDT管理
status: active
---

# DSP MDTCTX（显示MDT上下文）

## 功能

**适用网元：MME**

此命令用于查看MDT上下文的相关信息。

## 注意事项

- 该命令执行后立即生效。
- 当不存在用户上下文时，该命令查询不到MDT上下文。
- 通过网管直接给MME创建MDT任务需要等用户切换到连接态才可以查询到MDT参数。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询MDT上下文的方式。<br>取值范围：枚举类型。<br>- “BYIMSI（指定IMSI）”：表示根据IMSI查询用户的MDT上下文。<br>- “MDTUSRNUM（MDT用户数）”:表示查询MDT用户数。<br>- “ALL（全部）”：表示全部查询<br>默认值：<br>“BYIMSI（指定IMSI）” |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数为国际移动用户标识。<br>前提条件：该参数在<br>“查询方式”<br>参数配置为指定为<br>“BYIMSI”<br>后生效。<br>取值范围：0~15位十进制数字。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MDTCTX]] · MDT上下文（MDTCTX）

## 使用实例

查询IMSI号为123032201000001的用户的MDT上下文的相关信息

DSP MDTCTX: QUERYOPT=BYIMSI, IMSI="123032201000001";

```
+++    usn        2017-12-15 17:40:56+08:00
O&M   #117
%%DSP MDTCTX: QUERYOPT=BYIMSI, IMSI="123032201000001";%%
RETCODE = 0  操作成功

操作结果如下：
--------------
              IMSI  =  
123032201000001

            跟踪号  =  41006
        跟踪触发源  =  HSS
          任务类型  =  Immediate MDT only
      测量区域类型  =  TAI
      测量区域列表  =  123301234; 1230300134; 123300334
          测量方式  =  1
      报告触发类型  =  1
          报告间隔  =  12分钟
          报告次数  =  4
      RSRP事件阈值  =  0
      RSRQ事件阈值  =  0
Logged MDT报告间隔  =  NULL
Logged MDT持续时间  =  NULL
      MDT PLMN列表  =  12330; 12310; 12320
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MDTCTX.md`

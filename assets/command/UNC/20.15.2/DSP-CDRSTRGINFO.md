---
id: UNC@20.15.2@MMLCommand@DSP CDRSTRGINFO
type: MMLCommand
name: DSP CDRSTRGINFO（查询缓存话单信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CDRSTRGINFO
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费缓存
- 缓存信息
status: active
---

# DSP CDRSTRGINFO（查询缓存话单信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用于查看硬盘计费缓存文件的情况，如果在命令中指定PODNAME，则显示指定PODNAME的硬盘的计费缓存情况，若不指定，则返回所有硬盘的计费缓存情况。

## 注意事项

如果手动进行了话单删除，命令回显信息可能需要10分钟才能刷新。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STGTYPE | 缓存类型 | 可选必选说明：必选参数<br>参数含义：缓存类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CHGCDR：离线计费话单。<br>- CHGMSG：融合计费消息。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRSTRGINFO]] · 缓存话单信息（CDRSTRGINFO）

## 使用实例

查询PODNAME为uncpod-0的硬盘的计费缓存情况：

```
%%DSP CDRSTRGINFO: STGTYPE=CHGCDR, PODNAME="uncpod-0";
```

```
%%
RETCODE = 0  操作成功

离线计费话单缓存信息
--------------------
               POD名称  =  uncpod-0
              缓存类型  =  chgcdr
剩余硬盘空间（兆字节）  =  10079
    剩余硬盘空间百分比  =  83
     正确R98话单文件数  =  0
     正确R99话单文件数  =  0
      正确R4话单文件数  =  0
      正确R5话单文件数  =  0
      正确R6话单文件数  =  0
      正确R7话单文件数  =  0
   正确R8PGW话单文件数  =  0
  正确R8 SGW话单文件数  =  0
  正确R9 PGW话单文件数  =  0
  正确R9 SGW话单文件数  =  0
 正确R10 PGW话单文件数  =  0
 正确R10 SGW话单文件数  =  0
正确AAA stop消息文件数  =  0
    正确计费缓存文件数  =  0
    损坏计费缓存文件数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CDRSTRGINFO.md`

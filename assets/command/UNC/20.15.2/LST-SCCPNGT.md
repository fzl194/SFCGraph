---
id: UNC@20.15.2@MMLCommand@LST SCCPNGT
type: MMLCommand
name: LST SCCPNGT（查询SCCP新全局翻译码）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCCPNGT
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP新全局翻译码
status: active
---

# LST SCCPNGT（查询SCCP新全局翻译码）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来查询SCCP新全局码表指定记录的信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTX | 新GT码索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定新GT码对应的索引值。<br>取值范围：0~4095<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPNGT]] · SCCP新全局翻译码（SCCPNGT）

## 使用实例

查询SCCP新全局翻译码中的所有记录：

LST SCCPNGT:;

```
%%LST SCCPNGT:;%% 
RETCODE = 0  操作成功。

SCCP新全局翻译码表
------------------
 新GT码索引  GT码表示语  ITU翻译类型  翻译类型  编号计划           地址性质表示语  地址信息  编码设计  描述    

 1           ITU四类     0            NULL      ISDN/电话编号计划  国际号码        123       奇位数    FOR HLR1
 2           ITU四类     0            NULL      数据编号计划       空闲            124       奇位数    FOR HLR2
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCCP新全局翻译码(LST-SCCPNGT)_72345929.md`

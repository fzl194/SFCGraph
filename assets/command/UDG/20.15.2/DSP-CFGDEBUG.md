---
id: UDG@20.15.2@MMLCommand@DSP CFGDEBUG
type: MMLCommand
name: DSP CFGDEBUG（显示CFG诊断日志）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CFGDEBUG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 配置维护
- 配置数据
status: active
---

# DSP CFGDEBUG（显示CFG诊断日志）

## 功能

该命令用于显示CFG诊断日志。

## 注意事项

该命令仅用于研发问题定位。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEBUGTYPE | 调试类型 | 可选必选说明：必选参数<br>参数含义：调试类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：<br>- 0: 关键信息的日志，包括关键步骤和出错的日志。<br>- 1: APPCFG侧记录指定类下发信息。<br>- 3: APPCFG侧记录数据下发出错信息。<br>- 4: ADM侧记录数据下发出错信息。<br>- 5: APPCFG基础组件配置恢复情况：通知各个组件APPDB就绪记录。<br>- 6: APPCFG基础组件配置恢复情况：请求APPDB与配置恢复请求记录。<br>- 7: CFG配置编辑失败记录。<br>- 8: ECM记录正在运行的脚本信息。<br>- 9: ECM记录历史脚本信息。<br>- 10: ADM下发记录。<br>- 11: CFG内部配置记录。<br>- 12: 进程内CMF内存占用情况。<br>- 13: ECM运行出错记录。<br>- 15: 进程内注册的符号表。<br>- 16: 请求APPDB记录。<br>- 17: 请求APPDATA记录。<br>- 18: 组件状态订阅记录。<br>- 19: CMF进程事件信息。<br>- 20: 用户操作日志。<br>- 21: CFG进程的local数据。<br>- 22: 正在使用的DB查询句柄。<br>- 23: 查看黑匣子列表。<br>- 24: 查看黑匣子内容。<br>- 26: 查看黑匣子的内容摘要。<br>- 27: 查看事务仓库中的数据。<br>- 28: 历史有问题的脚本信息。<br>- 29: 获得当前所有可维护信息的持久化信息。<br>- 30: APPCFG记录普通组件配置恢复。<br>- 31: APPCFG状态切换。<br>- 32: 备份事务信息。<br>- 33: 记录配置下发可靠性相关的COCKET信息。<br>- 34: MIMLIB运行出错记录。<br>- 35: 复制可维护性文件到版本home目录。<br>- 36: ID2NAME缓存数据。<br>- 37: APPDB后台保存轨迹记录。<br>- 38: LUA脚本中的断言信息。<br>- 39: LSVS运行出错记录。<br>- 40: LSVS运行轨迹记录。<br>- 41: 脚本老化信息。<br>- 43: DAM写入APPDB超过1秒的记录。<br>- 44: 回退点文件操作信息。<br>- 45: 用户操作session信息。<br>- 46: APPDB内存占用情况。<br>- 47: CFG配置锁记录。<br>- 48: 性能统计开关。<br>- 49: 数据库操作记录。<br>- 50: AppTrans信息。<br>- 51: SubTrans信息。<br>- 52: CFG内部配置记录统计。<br>- 53: 进程内所有DB内存占用情况。<br>- 54: VRPFILE文件读写可维护性。<br>- 55: COCKET消息丢弃可维护性。<br>- 56: CFG状态机。<br>- 57: 保存指定进程的APPDB到磁盘。<br>- 58: APP脚本执行性能信息。<br>- 59: DB API执行性能信息。<br>- 60: 配置变更点操作轨迹。<br>- 61: CTRLC事务维护信息。<br>- 62: 配置试运行状态记录。<br>- 64: ECM订阅的组件状态信息。<br>- 65: APPDB与RDB一致性校验结果历史记录。<br>- 66: 回退点管理文件变更信息。<br>- 67: 自动保存的信息。<br>- 68: 配置增量点信息。<br>- 69: 字节序翻转历史记录。<br>- 70: ADM DIM下发处理信息。<br>- 71: BuildRun更新信息。<br>- 72: DBMS状态机。<br>- 73: 动态数据生产者信息。<br>- 74: 动态数据消费者信息。<br>- 75: 请求CFG侧配置数据。<br>- 76: CFG备份丢失消息记录。<br>- 77: CFG侧下发记录。<br>- 78: ADM多线程信息。<br>- 79: Commit回调信息。<br>- 80: BuildRun模板段类型信息。<br>- 81: DB翻译记录。<br>- 82: APPCFG侧APPDATA校验信息。<br>- 83: 正常工作流的日志。<br>- 84: BuildRun显示信息。<br>- 85: BuildRun类信息。<br>- 86: 执行耗时过长的脚本。<br>- 87: BuildRun矩阵信息。<br>- 88: BuildRun默认记录信息。<br>- 89: BuildRun master类信息。<br>- 90: BuildRun无数据的类信息。<br>- 91: BuildRun DOM关系信息。<br>- 92: BuildRun DOM类信息。<br>- 93: BuildRun DOM查询链接信息。<br>- 94: BuildRun搜索树信息。<br>- 95: BuildRun实例树信息。<br>- 96: ADM记录的平滑轨迹信息。<br>- 97: ADM记录的平滑事件信息。<br>- 98: APPCFG记录的平滑轨迹信息。<br>- 99: APPCFG记录的平滑事件信息。<br>- 100: 平滑模型检查信息。<br>- 101: 非法内部配置信息。<br>- 102: 资源补丁轨迹信息。<br>- 103: RDB和master的检查结果。<br>- 104: ADM记录的平滑状态信息。<br>- 105: OCL检查失败的历史信息。<br>- 106: VNFC操作轨迹。<br>- 107: VNFC运行轨迹。<br>- 108: 网元备份与恢复操作轨迹。<br>- 109: 扩减容轨迹。<br>- 110: BuildRun的multi-class信息。<br>- 111: Builrun的段类型信息。<br>- 112: APPCFG记录的平滑会话信息。<br>- 113: 平滑结果的历史信息。<br>- 114: BuildRun二级特性信息。<br>- 115: BuildRun脚本信息。<br>- 116: BuildRun的类到段类型的映射信息。<br>- 117: 将BuildRun全量信息写入文件。<br>- 118: 将BuildRun全量信息输出到屏幕。<br>- 119: 打印BuildRun摘要信息。<br>- 120: BuildRun错误信息。<br>- 121: SOP跟踪信息。<br>- 123: SOP跟踪刷新信息。<br>- 124: SOP LIB库信息。<br>- 125: SOP会话信息。<br>- 126: SOP Box信息。<br>- 129: SOP序列LIB信息。<br>- 130: SOP序列表信息。<br>- 131: SOP序列输入信息。<br>- 132: SOP序列输出信息。<br>- 139: ADM维护的APPCFG状态信息。<br>- 140: APP进程与中心数据差异（RUNNING DATA）。<br>- 160: BuildRun补丁维护信息。<br>- 162: 查看类跟踪信息开关。<br>- 163: 设置类跟踪信息的条件。<br>- 164: 查看类跟踪的结果。<br>- 165: 查看配置过程跟踪信息开关。<br>- 166: 查看配置过程跟踪信息结果。<br>- 167: 查看配置提交信息。<br>- 168: 查看进程校验码信息。 |
| LOCINDEX1 | 进程ID | 可选必选说明：必选参数<br>参数含义：进程ID（当在VNFP服务实例上执行该命令时，该参数通过<br>[**DSP RESPROCESSINFO**](../../../../../单体服务平台功能管理/操作维护/系统调测/进程和组件信息/显示进程信息（DSP RESPROCESSINFO）_04641826.md)<br>命令获取，其他服务实例上执行该命令时，该参数通过<br>[**DSP PROCESSINFO**](../../进程和组件信息/显示进程信息（DSP PROCESSINFO）_59103523.md)<br>命令获取）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| PARA1 | 参数一 | 可选必选说明：可选参数<br>参数含义：该参数表示类ID。DEBUGTYPE值为163时为必选，其他情况可选且参数不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PARA2 | 参数二 | 可选必选说明：可选参数<br>参数含义：该参数表示操作类型。DEBUGTYPE值为163时为可选且是生效参数，其他情况也可选但参数不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～9。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CFGDEBUG]] · CFG诊断日志（CFGDEBUG）

## 使用实例

显示CFG诊断日志：

```
DSP CFGDEBUG:DEBUGTYPE=4,LOCINDEX1=3
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
查询结果  

                                                                                                                                                                                                                                       
*************************************BEGIN*************************************

The commit error from adm: 
TransNo SsnID CommitTimeStamp SpendTime(ms) AppCid AppOwnerCid AppCompInsance DamClassId DimClassId InstId OpType SelfRetCode CommitRetCode IsRollback IsInQueue

*************************************END***************************************
 
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-CFGDEBUG.md`

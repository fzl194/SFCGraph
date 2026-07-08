---
id: UNC@20.15.2@MMLCommand@LST LCSPARAEX
type: MMLCommand
name: LST LCSPARAEX（查询LCS扩展参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LCSPARAEX
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCS扩展参数
status: active
---

# LST LCSPARAEX（查询LCS扩展参数）

## 功能

**适用网元：MME**

该命令用于查询LCS扩展参数。

## 注意事项

- 无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商标识<br>数据来源：整网规划<br>取值范围：0~64,128~254<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LCSPARAEX]] · LCS扩展参数（LCSPARAEX）

## 使用实例

1. 查询NOID为0的运营商的LCS扩展参数。
  LST LCSPARAEX: NOID=0;
  ```
  %%LST LCSPARAEX: NOID=0;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
                     运营商标识  =  0
          紧急呼叫NI-LR支持开关  =  开
             GMLC选择策略组索引  =  1
                       上报类型  =  定位上报
           是否支持缺省承载呼叫  =  不支持
           创建承载时间间隔(秒)  =  2
       紧急呼叫释放是否触发上报  =  否
                     HO上报类型  =  源侧上报
  和E-SMLC交互前是否启动LRC流程  =  是
  和E-SMLC交互后是否启动LRC流程  =  是
                       水平精度  =  19
                       响应时间  =  低时延
                       移动速度  =  请求
                           描述  =  noname
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询LCS扩展参数(LST-LCSPARAEX)_72225495.md`
